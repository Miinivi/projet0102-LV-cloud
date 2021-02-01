import pandas as pd
import numpy as np

# Code in english
# Commentaire en français
class Data:
    """
        Récupérer les données du dossier local
    """
    def __init__(self):
        """
            Dataset
        """
        print("Initialisation des données")
        self.dt = None
        print("Processus réussi")

    def get_data(self):
        print("Chargement des données")
        self.dt = pd.read_csv("vaccination_tweets.csv")
        print("Données chargées")

from joblib import dump,load
# Joblib https://joblib.readthedocs.io/en/latest/

class MBuilder:
    """
        Modèle du machine learning
    """
    def __init__(self, model_path:str=None, save:bool=None):
        self.model_path = model_path
        self.save = save
        self.reg = RandomForestRegressor()
        print ("MBuilder réussi")

    def __repr__(self):
        pass
    
    def train(self, X, y):
        self.reg.fit(X,y)
        print("Algorithme réussi")

    def predict_test(self, X) -> np.ndarray: 
        return self.reg.predict(X.iloc[:1])

    def save_model(self, path:str):
        dump(self.reg, '{}/model.joblib'.format(path))
        self.save = True
        print('Fichier sauvegardé')

    def predict_from_dump(self, X) -> np.ndarray:
        return self.reg.predict(X)

    def print_accuracy(self,X_test,y_test):
        score = self.reg.score(X_test,y_test)*100
        print('Régression de {}%'.format(score))

    def load_model(self):
        try:
            self.reg = joblib.load("{}/model.joblib".format(self.path))
            print("Chargement fichier réussi")
        except:
            print("Fichier non trouvé")
