# PySpark Starter

Ce repo est un boostrap pour des Jobs Pyspark

## Utilisation

### Pour créer un nouveau job

il faut rajouter un modules dans le dossier *src/jobs/*. Le module devra obligatoirement contenir une methode appelées analyze

### Pour lancer un job:

```bash
cd dist/
spark-submit --py-files jobs.zip main.py --job-name "nom du job à lancer" --job-args "arguments pour le job"
```

## TO DO
* Ajouter un fichier de configuration pour rensigner toutes les infos du job: nom, master, mode d'execution, fichier de donnée ....
* Ajouter le support pour les SparkContext et les SparkSession 
* Ajouter un support pour variables broadcast ou les accumulator 
* Compléter le README