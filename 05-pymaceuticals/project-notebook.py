
# coding: utf-8

# # Pymaceuticals

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[2]:


mouse_drug_data_to_load = "data/mouse_drug_data.csv"
clinical_trial_data_to_load = "data/clinicaltrial_data.csv"


# In[3]:


mouse_drug_data = pd.read_csv(mouse_drug_data_to_load)
mouse_drug_data.head()


# In[4]:


clinical_data = pd.read_csv(clinical_trial_data_to_load)
clinical_data.head()


# In[5]:


combined_clinical_data = pd.merge(clinical_data, mouse_drug_data, how="left", on=["Mouse ID", "Mouse ID"])
combined_clinical_data.head()


# ## Tumor Response to Treatment

# In[6]:


avg_tumor_volume_by_drug_and_timepoint = combined_clinical_data.groupby(['Timepoint', 'Drug']).mean()['Tumor Volume (mm3)']
avg_tumor_volume_by_drug_and_timepoint_df = pd.DataFrame(avg_tumor_volume_by_drug_and_timepoint)
avg_tumor_volume_by_drug_and_timepoint_df = avg_tumor_volume_by_drug_and_timepoint_df.reset_index()
avg_tumor_volume_by_drug_and_timepoint_df.head()


# In[7]:


sem_tumor_volume_by_drug_and_timepoint = combined_clinical_data.groupby(['Timepoint', 'Drug']).sem()['Tumor Volume (mm3)']
sem_tumor_volume_by_drug_and_timepoint_df = pd.DataFrame(sem_tumor_volume_by_drug_and_timepoint)
sem_tumor_volume_by_drug_and_timepoint_df = sem_tumor_volume_by_drug_and_timepoint.reset_index()
sem_tumor_volume_by_drug_and_timepoint_df.head()


# In[8]:


tumor_volume_avg_pivot = avg_tumor_volume_by_drug_and_timepoint_df.pivot(index='Timepoint', columns="Drug")['Tumor Volume (mm3)']
tumor_volume_avg_pivot


# In[9]:


tumor_volume_sem_pivot = sem_tumor_volume_by_drug_and_timepoint_df.pivot(index='Timepoint', columns="Drug")['Tumor Volume (mm3)']
tumor_volume_sem_pivot


# In[10]:


errorbar_attr = {
    'markersize': 5,
    'linestyle': "dashed",
    'linewidth': 0.50,
}
plt.errorbar(
    tumor_volume_avg_pivot.index,
    tumor_volume_avg_pivot["Capomulin"],
    yerr=tumor_volume_sem_pivot["Capomulin"],
    color="r",
    marker="o",
    **errorbar_attr
)
plt.errorbar(
    tumor_volume_avg_pivot.index,
    tumor_volume_avg_pivot["Infubinol"],
    yerr=tumor_volume_sem_pivot["Infubinol"],
    color="b",
    marker="^",
    **errorbar_attr
)
plt.errorbar(
    tumor_volume_avg_pivot.index,
    tumor_volume_avg_pivot["Ketapril"],
    yerr=tumor_volume_sem_pivot["Ketapril"],
    color="g",
    marker="s",
    **errorbar_attr
)
plt.errorbar(
    tumor_volume_avg_pivot.index,
    tumor_volume_avg_pivot["Placebo"],
    yerr=tumor_volume_sem_pivot["Placebo"],
    color="k",
    marker="d",
    **errorbar_attr
)

plt.title("Tumor Response to Treatment")
plt.ylabel("Tumor Volume (mm3)")
plt.xlabel("Time (Days)")
plt.grid(True)
plt.legend(loc="best", fontsize="small", fancybox=True)
plt.show()


# ## Survival Rates

# In[11]:


survival_count = combined_clinical_data.groupby(['Drug', 'Timepoint']).count()['Mouse ID']
survival_count_df = pd.DataFrame(survival_count)
survival_count_df = survival_count_df.reset_index()
survival_count_df_pivot = survival_count_df.pivot(index='Timepoint', columns='Drug')['Mouse ID']


# In[12]:


# survival_count_df_pivot_normalized = survival_count_df_pivot.apply(
#     lambda row: row/25
# )
survival_count_df_pivot_normalized = survival_count_df_pivot.div(
    survival_count_df_pivot.iloc[0,:].values
)
survival_count_df_pivot_normalized


# In[13]:


plot_attr = {
    'linestyle': 'dashed',
    'markersize': 5,
    'linewidth': 0.50,
}
plt.plot(
    100 * survival_count_df_pivot_normalized["Capomulin"],
    "ro", 
    **plot_attr
)
plt.plot(
    100 * survival_count_df_pivot_normalized["Infubinol"],
    "b^",
    **plot_attr,
)
plt.plot(
    100 * survival_count_df_pivot_normalized["Ketapril"],
    "gs",
    **plot_attr
)
plt.plot(
    100 * survival_count_df_pivot_normalized["Placebo"],
    "kd",
    **plot_attr
)
plt.title("Survival During Treatment")
plt.ylabel("Survival Rate (%)")
plt.xlabel("Time (Days)")
plt.grid(True)
plt.legend(loc="best", fontsize="small", fancybox=True)
plt.show()

