# Databricks notebook source
dbutils.secrets.list("formula1-scope")

# COMMAND ----------

storage_account_name = "formula1fotisdl"
dbutils.secrets.help()
dbutils.secrets.listScopes()
dbutils.secrets.list("formula1-scope")
client_id            = dbutils.secrets.get(scope="formula1-scope", key="clientid")
tenant_id            = dbutils.secrets.get(scope="formula1-scope", key="tenantid")
client_secret        = dbutils.secrets.get(scope="formula1-scope", key="clientsecret")

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{client_secret}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

def mount_adls(container_name):
  dbutils.fs.mount(
    source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_account_name}/{container_name}",
    extra_configs = configs)

# COMMAND ----------

#dbutils.fs.unmount('/mnt/formula1fotisdl/raw')
# dbutils.fs.unmount('/mnt/formula1fotisdl/processed')

mount_adls('raw')
mount_adls('processed')


# COMMAND ----------

mount_adls('presentation')

# COMMAND ----------

mount_adls('demo')

# COMMAND ----------

dbutils.fs.ls("/mnt/formula1fotisdl/processed")

# COMMAND ----------

dbutils.fs.ls("/mnt/formula1fotisdl/raw")

# COMMAND ----------

dbutils.fs.ls("/mnt/formula1fotisdl/presentation")

# COMMAND ----------


