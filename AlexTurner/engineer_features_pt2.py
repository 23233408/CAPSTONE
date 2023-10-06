from definitions import *

# end of df
def transform(self, df):
        df['qSOFA'] = self.qsofa_score(df)
        df['SOFA'] = self.sofa_score(df)
        return df

def sofa_updater(self, data, range, reverse=False):
        s = pd.Series(index=df.index)
        for i in range(len(range) - 1):
            upper, lower = range[i], range[i+1]
            s[lower <= data < upper] = i
        return s

class InSightFeatures(BaseIDTransformer):
    """
    Gets the insight features for each unique id.
    
    
    """
    def __init__(self, window_size=3):
        self.window_size = window_size  # Num prev entries to look at. The paper used 3.

    def transform_id(self, df):
        # Get the values at time now and two timepoints prior
        df_values = self.add_previous_times(df, self.window_size)

        # Get the differences x0 - x1 and x1 - x2
        df_differences = self.add_previous_differences(df, self.window_size - 1)

        # Concat together to make InSight features
        df_insight_features = pd.concat([df_values, df_differences], axis=1)

        return df_insight_features


    def add_previous_times(df, n_times):
        """
        Adds the previous times to the current time for each row in a dataframe. Relabels cols accordingly. Rows now have
        the form:
            row_i -> x0_t, ... xk_t, x0_t-1, ..., xk_t-n_times
        :param df: the dataframe
        :param n_times: The number of times to have in the same row
        :return: df with time vals and appropriately labelled columns
        """
        df_new = pd.concat([df.shift(i) for i in range(n_times)], axis=1)
        df_new.columns = [column + '.prev({})'.format(i) for i in range(n_times, 0, -1) for column in df.columns]
        return df_new


    def add_previous_differences(df, n_differences):
        """
        Adds differences between rows. If a rows x0, x1, x2 and n_differences set to 2, returns a df with rows that contain
        entries x0 - x1, x1 - x2.
        :param df: dataframe
        :param n_differences: number of differences to add
        :return: differences df
        """
        df_new = pd.concat([df.shift(i) - df.shift(i+1) for i in range(n_differences)], axis=1)
        df_new.columns = [column + '.diff({},{})'.format(i-1, i) for i in range(n_differences, 0, -1) for column in df.columns]
        return df_new




# People with SIRS criteria are twice as likely to have sepsis
if __name__ == '__main__':
    df = load_pickle(DATA_DIR + '/interim/munged/df.pickle')
    # df = CalculateSofa().transform(df)
    df = SIRSLabeller().transform(df)