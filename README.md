#IPython Notebook for PySpark Setup

##Requirement

1. IPython 3.x. There is problem with profiles for IPython 4.0 after the Big Split.
2. Spark > 1.3.0


##Usage

Copy this script that bring up IPython notebook server daemon to a location.

- spark_notebook.py --> `<your_path>`/spark_notebook.py

Remember to modify the sections marked with XXX to change default notebook home.

`python spark_notebook.py` would start the IPython Notebook for PySpark. That's it.

If you want IPython Notebook auto-start on boot, you can do the following steps for Ubuntu.

Copy upstart autostart scripts and conf to the following locations, change the sections marked with XXX to match your setup and `spark_notebook.py` path.

- notebook --> /etc/init.d/notebook
- notebook.conf --> /etc/init/notebook.conf

##Note

First time running the `spark_notebook.py` would generate the IPython Notebook profile.

- profile_pyspark --> ~/.ipython/profile_pyspark

##Troubleshoot
1. If `python spark_notebook.py` complains about "No such notebook dir:" error, then probably you forget to change the notebook_dir variable in `spark_notebook.py` file.
2. If you had trouble bringing spark_notebook.py, you can check `/var/log/upstart/notebook` for logs.
