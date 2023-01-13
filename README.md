# abcd2_data_wrangling

Preparing ABCD2 study data for reporting

1. consensus_amyloid_pos.ipynb: Establish Amyloid consensus result based on PET scan reads (pet_read.csv) and quantitative result (allamyloid_DATE_with_compSUVR.csv)
2. Tau_mri.ipynb: Add Amyloid consensus to Tau (ABC_TauPET_MRI3T_ASHST1T2_measurements_DATE.csv) and MRI data (ABC_MRI3T_ASHST1T2_measurements_DATE.csv) (MRI data done two ways)
3. imaging_by_the_numbers.ipynb & subject_scans_bystudy.py: count of scan types by subject for ABC and ABCD2, subcategories of Amyloid negative and longitudinal subjects.