
# # for any null values it sets that value to the most common value in column


# def drop_null_values(feature):
#     df[feature] = df[feature].fillna(df[feature].mode()[0])


# features = df.columns[1:-1]  # excludes id and sales price
# for feature in features:
#     drop_null_values(feature)

# y = df["SalePrice"]
# X = df[features]
# X = pd.get_dummies(data=X, drop_first=True)
# reg = linear_model.LinearRegression()
# reg.fit(X, y)
# r2 = reg.score(X, y)
# predictions = reg.predict(X)
# y = df["SalePrice"]
# # print(r2)
# sns.regplot(x=predictions, y=y)

# plt.show()
