"""
Model fitting, tuning and evaluation pipeline.

Below extract are functions I contributed during the project 
(for complete modelling pipeline, please refer to the "modelling_pipeline.py" in src directory)
"""

class ModelPipeline:

    # Init parameters
    ROOT_DIR = Path('../..')
        
    def __init__(self, ROOT_DIR):
        self.ROOT_DIR = ROOT_DIR
        # plot output
        self.output_dir = self.ROOT_DIR / 'output' / 'plots'
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def get_full_dfs(self, tops):
        dfs_dict = {}
        for top in tops:
            dfs_dict[f"top{top}"] = self.get_model_full_dfs(f'top{top}')
        return dfs_dict

    def get_model_full_dfs(self, top, timepoints=['t0', 't1', 't2', 't3', 't4']):
        
        """
        Function to read the model input dataframes based on provided prefixes and date string.
        
        Parameters:
        - ROOT_DIR: The root directory path.
        - prefix: The prefix (e.g. 'top20', 'top30', etc.)
        - timepoints: A list of timepoints (default is ['t0', 't1', 't2', 't3', 't4']).
        
        Returns:
        - A dictionary with keys as timepoints and values as the corresponding dataframes.
        """
        
        dfs = {}
        for tp in timepoints:
            path = self.ROOT_DIR / 'data' / 'full_data' / f"{tp}_{top}.csv"
            dfs[tp] = self.get_model_input_df(path)
        
        return dfs

    def count_missing_values_all(self, dfs_dict, hours_list, top_n_features, sepsis_only = False):
        """
        Get count of missing values for all DF in dictionary. 
                
        Args:
            dfs_dict (Dict): Dictionary of data extractions at different time points.
            hours_list (_type_): _description_
            top_n_features (_type_): _description_
            sepsis_only: Only account for Sepsis admissions or All admissions

        Returns:
            result_df (DataFrame): NA Counts and NA Proportions
        """
        # Initialise dataframes to store results
        na_counts = pd.DataFrame(index=hours_list, columns=[f'top{n}_features_NA_Count' for n in top_n_features])
        na_proportions = pd.DataFrame(index=hours_list, columns=[f'top{n}_features_NA_%' for n in top_n_features])

        # Iterate through input dictionary
        for top_n_key, time_dfs in dfs_dict.items():
            for time_point, df in time_dfs.items():
                if sepsis_only == True:
                    df = df[df['IS_SEPSIS'] == 1]
                    
                df_without_target = df.drop(columns=['IS_SEPSIS'])
                total_values = df_without_target.size
            
                # count missing
                count_999 = (df_without_target == -999).sum().sum()
                missing_proportions = count_999 / total_values * 100
                formatted_missing_proportions = "{:.2f}%".format(missing_proportions)

                # Extract the hour and top_n from the keys
                hour = int(time_point.lstrip('t'))  # remove 't' and convert to int
                top_n = int(top_n_key.lstrip('top'))  # remove 'top' and convert to int
                
                # Store results in dataframes
                na_counts.loc[hour, f'top{top_n}_features_NA_Count'] = count_999
                na_proportions.loc[hour, f'top{top_n}_features_NA_%'] = formatted_missing_proportions

        result_df = pd.DataFrame(index=hours_list)

        # Concatenate the data for each top_n features
        for top_n in top_n_features:
            na_count_col = f'top{top_n}_features_NA_Count'
            na_prop_col = f'top{top_n}_features_NA_%'
            result_df[na_count_col] = na_counts[na_count_col]
            result_df[na_prop_col] = na_proportions[na_prop_col]

        result_df.index = ['t' + str(i) for i in result_df.index]

        return result_df
        
        #return na_counts, na_proportions

    def count_missing_SOFA(self, dfs_dict, hours_list, sepsis_only=False):
        """
        Get count of missing SOFA for all DF in dictionary. 
                
        Args:
            dfs_dict (Dict): Dictionary of data extractions at different time points.
            hours_list (_type_): _description_
            sepsis_only (bool): Only account for Sepsis admissions or All admissions

        Returns:
            result_df (DataFrame): NA Counts and NA Proportions
        """
        # Initialise dataframes to store results
        na_counts = pd.DataFrame(index=hours_list, columns=['SOFA_NA_Count'])
        na_proportions = pd.DataFrame(index=hours_list, columns=['SOFA_NA_%'])

        # Iterate through input dictionary
        for _, time_dfs in dfs_dict.items():
            for time_point, df in time_dfs.items():
                if sepsis_only:
                    df = df[df['IS_SEPSIS'] == 1]
                    
                total_SOFA = df.shape[0]
            
                # count missing SOFA values
                count_SOFA_999 = (df['SOFA'] == -999).sum()
                missing_proportions = count_SOFA_999 / total_SOFA * 100
                formatted_missing_proportions = "{:.2f}%".format(missing_proportions)

                # Extract the hour
                hour = int(time_point.lstrip('t'))  # remove 't' and convert to int
                
                # Store results in dataframes
                na_counts.loc[hour, 'SOFA_NA_Count'] = count_SOFA_999
                na_proportions.loc[hour, 'SOFA_NA_%'] = formatted_missing_proportions

        result_df = pd.DataFrame(index=hours_list)
        result_df['SOFA_NA_Count'] = na_counts['SOFA_NA_Count']
        result_df['SOFA_NA_%'] = na_proportions['SOFA_NA_%']
        result_df.index = ['t' + str(i) for i in result_df.index]

        return result_df

    def get_class_weights(self, y_train):
        """
            Compute class weights for balancing the classes in the target variable.

        Args:
            y_train (_type_)

        Returns:
            class_weights (dict)
        """
        # Get sepsis label proportions
        label_counts = y_train.value_counts()
        label_proportions = label_counts / len(y_train)*100
        
        # Compute class weights
        class_weights = {0: 1 / (label_proportions[0] / 100), 1: 1 / (label_proportions[1] / 100)}

        # Round the class weights to the desired precision (optional)
        class_weights = {key: round(weight, 4) for key, weight in class_weights.items()}
        
        return class_weights

    def perform_cv_for_conditions(self, hours_list, top_n_features, split_data_dict, candidate_models, all_models=True, LR_only=False, RF_only=False, GB_only=False):
        """
        Performs cross-validation for given conditions and data.
        
        Args:
            conditions (list of tuples): List of (top_features, time_window) conditions.
            split_data_dict (dict): Dictionary with data splits corresponding to conditions.
            models (dict): Candidate models to perform CV.
            mp (Module): Module that contains the cv_analysis function.
        
        Returns:
            pd.DataFrame: Consolidated results of CV for the conditions.
        """
        all_results = []

        for hour in hours_list:
            for top_n in top_n_features:    
                current_data = split_data_dict[(top_n, hour)]
                X_train = current_data['X_train']
                y_train = current_data['y_train']
                
                current_results = self.cv_analysis(X_train, y_train, candidate_models, all_models, LR_only, RF_only, GB_only)
                
                current_results['top_features'] = top_n
                current_results['time_window'] = hour
                
                all_results.append(current_results)

        return pd.concat(all_results, ignore_index=True)

    def cv_analysis_all(self, X_t0_train, y_t0_train, 
                                X_t1_train, y_t1_train,
                                X_t2_train, y_t2_train,
                                X_t3_train, y_t3_train,
                                X_t4_train, y_t4_train, candidate_models, hours_list, top_n_features):
        """
        Perform cross-validation analysis on a set of candidate models and return their mean scores.

        Args:
            X_train (pd.DataFrame): Scaled feature matrix for training.
            y_train (pd.Series): Target labels for training.
            candidate_models (Dict[str, Any]): A dictionary of static ML model names and their respective instantiated models.
            class_weights (Dict[int, float]): A dictionary of class weights for handling sepsis class imbalance.
            
        Returns:
            pd.DataFrame: A DataFrame containing model names and their average cross-validation scores.
        """
        
        results = [] 
        
        for hour in hours_list:
            X_train = eval(f"X_t{hour}_train")
            y_train = eval(f"y_t{hour}_train")

            for top_n in top_n_features:
                # Calculate mean scores using cross validation
                for model_name, model in candidate_models.items():
                    scores = cross_val_score(model, X_train, y_train, scoring = 'balanced_accuracy', cv=3)
                    average_score = scores.mean()
                    results.append({
                        'model': f"{model_name}_{top_n}",
                        f't{hour}': average_score
                    })
                    
        df_model = pd.DataFrame(results)
                
        # Calculate overall average balanced accuracy for each model
        df_model['overall_avg_balanced_acc'] = df_model[['t0', 't1', 't2', 't3', 't4']].mean(axis=1)

        return(df_model)

    def tune_hyperparameters_rf(self, X_train, y_train, class_weights, model):
        """    
        Tune hyperparameters for Random Forest classifiers using GridSearchCV.

        Args:
            X_train (pd.DataFrame or np.array): Feature matrix for training.
            y_train (pd.Series or np.array): Target labels for training.
            class_weights (dict): Class weights for handling class imbalance.
            candidate_models:

        Returns:
            dict: Best parameters for each classifier.
        """  

        # define hyperparameter grid
        param_grid = {'n_estimators': [50, 100, 150], 
                      'max_depth': [10, 20, 30, 40], 
                      'min_samples_split': [2, 25, 50, 100, 250, 400],
                      'min_samples_leaf': [2, 25, 50, 100, 250, 400]
        }
        
        grid_search = GridSearchCV(estimator=model, param_grid=param_grid, scoring='balanced_accuracy', cv=3)
        grid_search.fit(X_train, y_train)

        best_params = grid_search.best_params_

        # Get best score
        print("Best parameters:", best_params)
        print("Best cross-validation score: {:.4f}".format(grid_search.best_score_))
            
        return best_params