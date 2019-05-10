import importlib
from pyspark.sql import SparkSession
import os
import sys
import argparse
import time

# Loading des jobs soit au format zip soit dans le dossiers jobs
if os.path.exists('jobs.zip'):
    sys.path.insert(0, 'jobs.zip')
else:
    sys.path.insert(0, './jobs')

if __name__ == "__main__":
    # Parsing des arguments de la ligne de commande
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", type=str, required=True, dest="job_name", help="The name of the module you want to launch.")
    parser.add_argument("--job-args", nargs="*", dest="job_args", help="Extra arguments for the job")
    args = parser.parse_args()

    print("Called with argument: {}".format(args))

    # Chargement des variables d'environement
    environement = {
        'PYSPARK_JOB_ARGS': ' '.join(args.job_args) if args.job_args else ''
    }

    job_args = dict()
    if args.job_args:
        job_args_tuples = [arg_str.split("=") for arg_str in args.job_args]
        print("job_args_tuple: {}".format(job_args_tuples))
        job_args = {a[0]: a[1] for a in job_args_tuples}
    print("Rnning job {}...\nEnv is {}\n".format(args.job_name, environement))
    os.environ.update(environement)

    # Création du spark context
    #sc = pyspark.SparkContext(appName=args.job_name)
    sc = SparkSession.builder.appName(args.job_name).getOrCreate()
    job_module = importlib.import_module("jobs.{}".format(args.job_name))

    # Running the job
    start = time.time()
    job_module.analyze(sc, **job_args)
    print("Execution time of {} was {} sec".format(args.job_name, time.time() - start))