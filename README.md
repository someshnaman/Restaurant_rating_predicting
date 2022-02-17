
# Restaurant Rating Prediction
>### **Problem Statement**

Whenever we go for a food application to order some 
the 1st thing that comes to our mind is that we order 
food where we get quality food. To accomplish that, whether the restaurant can provide quality food or not, we first look for the **Restaurant rating** and what other customers have mentioned about the restaurant food. Bengaluru is the IT capital of India. Most of the people here are dependent mainly on restaurant food as they don’t have time to cook for themselves. Therefore a platform is needed where one can put the several details of the restaurent and platform can predict about the rating of the restaurant as per the Historical data.


## User Interface
![alt text](https://github.com/someshnaman/Restaurant_rating_predicting/blob/main/templates/Demo.PNG?raw=true)
## Approach
The main goal is to predict the Rating of the Restarant.


<pre> 
<li> Data Exploration     : I started exploring dataset using pandas,numpy,matplotlib and seaborn. </li>
<li> Data visualization   : Ploted graphs to get insights about dependend and independed variables. </li>
<li> Feature Engineering  :  Removed missing values and created new features as per insights.</li>
<li> Model Selection I    :  1. Tested all base models to check the base accuracy.
                             2. Also ploted residual plot to check whether a model is a good fit or not.</li>
<li> Model Selection II   :  Performed Hyperparameter tuning using gridsearchCV and randomizedSearchCV.</li>
<li> Pickle File          :  Selected model as per best accuracy and created pickle file using joblib .</li>
<li> Webpage & deployment :  Created a webform that takes all the necessary inputs from user and shows output.
                                After that I have deployed project on heroku and AWS EC2/li></pre>
## Installation
-Steps to run this project

Step-1
- Change your directory in terminal 

Step-2
- Create a new environment

```bash
  conda Create --prefix ./env python=3.7 -y  
```
Step-3
- Activate the environment
```bash
  conda activate ./env   
```
- Install all the dependencies
```bash
  pip install -r requirements.txt
```

## Docker Link
**Link**: https://hub.docker.com/repository/docker/someshnaman/restaurentrating
## Technology Used
1. Python 
2. Sklearn
3. Flask
4. Html
5. Css
6. Pandas, Numpy 
7. Database 
8. Hosting
9. Docker
10. AWS
11. Circle CI 

## Documentation

[HLD](https://lnkd.in/eRJApNEs)

[LLD](https://lnkd.in/ekECvfNN)

[Architecture](https://lnkd.in/eMJch4BV)

[Wireframe](https://lnkd.in/eS7qSMSZ)



## Feedback

If you have any feedback, please reach out to me at chitranshisomesh@gmail.com


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/someshnaman)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/somesh-naman/)
