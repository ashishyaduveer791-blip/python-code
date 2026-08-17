import pandas as pd
from sklearn datasets import load_digits
digits=load_digits()

dir(digits)

%matplotlib inline
import matplotlib.pyplot as plt
plt.gray()
for i in range(4):
    plt.matshow(digits.image[i])

    digits.data[:5]

    df =pd.DataFrame(digits.data)

    df.head()
    df['target'] = digits.target
    df.head()

    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(df.drop(['target'],axis='columns'),digits.target,test_size =0.2)
    len(x_test)
    from sklearn.ensemble import RandomForestClassifier
    model=RandomForestClassifier()
    model.fit(x_train,y_train)

    model.score(x_test,y_train,y_train)

    y_predict=model.predict(x_test)
    t_predict=model.predict(x_test)

    from sklearn .metrics import confusion_matrix
    cm=confusion_matrix(y_test,y_predict)
    cm




