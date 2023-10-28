
time_points = ['t0', 't1', 't2', 't3', 't4']
train_test_data = [
    (X_t0_train, X_t0_test),
    (X_t1_train, X_t1_test),
    (X_t2_train, X_t2_test),
    (X_t3_train, X_t3_test),
    (X_t4_train, X_t4_test)
]

for time_point, (X_train, X_test) in zip(time_points, train_test_data):
    mp.generate_and_save_shap_plots(candidate_models, X_train, X_test, time_point)

_____

na_counts, na_proportions = mp.count_missing_values_all(dfs_dict, hours_list, top_n_features)


Stacking classifier - improves on the errors
Adaboost 