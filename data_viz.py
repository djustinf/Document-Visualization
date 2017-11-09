import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

def projectTo2D_TSNE(words, x_values):
    tsne = TSNE(n_components=2)
    x_tsne = tsne.fit_transform(x_values)    

    plt.scatter(x_tsne[:, 0], x_tsne[:, 1])
    
    for i, word in enumerate(words):
        plt.annotate(word, xy=(x_tsne[i, 0], x_tsne[i, 1]))

    plt.show()

def projectTo2D_PCA(words, x_values):
    pca = PCA(n_components=2)
    x_pca = pca.fit_transform(x_values)

    plt.scatter(x_pca[:, 0], x_pca[:, 1])
    
    for i, word in enumerate(words):
        plt.annotate(word, xy=(x_pca[i, 0], x_pca[i, 1]))

    plt.show()