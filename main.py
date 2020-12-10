from KohonenNN import KohonenNN as knn
from DataLoader import DataLoader as dl

l = dl()
nn = knn()
nn.learn(l.get_input())
