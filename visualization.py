import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df=pd.read_csv("C:/Users/BHAGWAN PATIL/Desktop/Ai-Ds/Datasets/Iris.csv")
# print(df)


#scatter plot

plt.scatter(df["PetalLengthCm"], df["PetalWidthCm"])
plt.title("Scatter Plot")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()



#Histogram plot

plt.hist(df["SepalWidthCm"])
plt.title("Histogram Plot")
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.show()



#Bar plot

sns.barplot(df["Species"]) #, df["PetalLengthCm"] ---depends on version old versions can take upto 2 i/p attributs
plt.title("Bar Plot")
plt.show()



#Pie Chart

mylabels=["Iris-setosa","Iris_versicolor","Iris-virginica"]
sizes=[50,50,50] #we give the sizes its not that smart to get it of there own
plt.pie(sizes, labels=mylabels) #, explode=(0.1,0.1,0.1) for spaces in-between
plt.axis('equal')
plt.show()


#count plot

sns.countplot(y='Species',data=df)  #x to change target attribute
plt.title("Count Plot For Species")
plt.show()


#Box Plot

sns.boxplot(y='Species',data=df)  #x to change target attribute.....   x for horizontal , y for vertical
plt.title("Count Plot For Species")
plt.show()


#Heatmap Plot
# delete last column for this
sns.heatmap(df.corr())
plt.show()
