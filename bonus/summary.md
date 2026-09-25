# CVRIE - Résumé rapide

## Objectif
CVRIE est un projet d'intelligence artificielle médicale visant à soutenir les équipes hospitalières sur deux tâches principales :

- classification supervisée d'images médicales ;
- regroupement non supervisé de témoignages patients par symptômes et gravité.

## Partie supervisée
Le dataset utilisé est un ensemble de radiographies pulmonaires avec les classes :

- NORMAL
- PNEUMONIA

Les images sont converties en niveaux de gris, redimensionnées puis divisées en ensembles d'entraînement et de test avec stratification. Plusieurs modèles sont comparés :

- Random Forest
- Régression Logistique
- KNN

> Le modèle retenu est le Random Forest, car il offre la meilleure performance globale et un bon équilibre pour cette tâche médicale.

## Partie non supervisée
La partie non supervisée utilise des témoignages patients non étiquetés. Les données sont nettoyées, transformées en matrice TF-IDF, puis regroupées à l'aide d'algorithmes de clustering.

Les modèles comparés incluent :

- K-Means
- Clustering hiérarchique
- MiniBatch K-Means

> Le K-Means est le modèle choisi comme meilleur compromis entre qualité de clustering et interprétabilité.

## Métrique clé
Pour le clustering, la métrique principale utilisée est le score de silhouette. Il permet de comparer la cohésion des clusters sans avoir de labels de vérité terrain.

## Conclusion
Ce projet montre une première version fonctionnelle de CVRIE, capable de :

- diagnostiquer une pneumonie sur des images radiographiques ;
- regrouper des témoignages de patients par similarité médicale.
