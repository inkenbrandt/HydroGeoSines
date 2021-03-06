
# Import packages
import numpy as np

# This package contains subroutines for the preprocessing of datasets

# Calculate temporal derivatives of GW data 
def calc_delta_GW(self): 
    return np.diff(self.GW.p)


# Calculate temporal derivatives of BA data 
def calc_delta_BA(self): 
    return np.diff(self.BA.p)

'''
Subroutines for future inclusion:

# Resample GW data
def resample_GW(self, hours): 
    print self.GW.p#[self.GW.t%hours==0]
    print self.GW.t#[self.GW.t%hours==0]
    return self.GW


# Resample BA data    
def resample_BA(self, hours): 
    self.BA.p = self.BA.p[self.BA.t%hours==0]
    self.BA.t = self.BA.t[self.BA.t%hours==0]
    return self.BA


# Remove data outliers    
def remove_outliers(self, dataset, threshold, direction): 
    # Function to remove outliers from input data, belongs to 
    # "preproc" subclass.
    if direction==LT:
        return dataset[dataset<threshold]
    elif direction==GT:
	return dataset[dataset>threshold]
    else:
	return error


# Fill data gaps using linear interpolation
def fill_gaps(self, dataset):
    return interpolate(dataset)


# Remove linear trend
def detrend_linear(self, dataset): 
    slope, intercept = regression(dataset)
    return dataset - slope*range(len(dataset))+intercept
    # Could include other detrending methods; e.g. moving average?


# Remove nonlinear trend
def detrend_nonlinear(self, dataset): 
    return
    
    
# Remove periodic trend
def detrend_periodic(self, dataset): 
    return
    

# Match manual measurements via offsets
def match_manual(self, dataset, manual_obs):
    return


# Calculate equivalent freshwater head from GW p measurements
def calc_fwhead(self): 
    return
'''