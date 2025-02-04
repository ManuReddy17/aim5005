import numpy as np
from typing import List, Tuple

class MinMaxScaler:
    def __init__(self):
        self.minimum = None
        self.maximum = None
        
    def _check_is_array(self, x: np.ndarray) -> np.ndarray:
        """
        Try to convert x to a np.ndarray if it's not a np.ndarray and return. If it can't be cast, raise an error.
        """
        if not isinstance(x, np.ndarray):
            x = np.array(x)
        assert isinstance(x, np.ndarray), "Expected the input to be a numpy array"
        return x
        
    def fit(self, x: np.ndarray) -> None:   
        x = self._check_is_array(x)
        self.minimum = x.min(axis=0)
        self.maximum = x.max(axis=0)
        
    def transform(self, x: np.ndarray) -> np.ndarray:
        """
        MinMax Scale the given vector
        """
        x = self._check_is_array(x)
        
        # Handle division by zero
        diff_max_min = self.maximum - self.minimum
        if np.any(diff_max_min == 0):
            return np.zeros_like(x)
        
        return (x - self.minimum) / diff_max_min

    def fit_transform(self, x: np.ndarray) -> np.ndarray:
        x = self._check_is_array(x)
        self.fit(x)
        return self.transform(x)
    
    
class StandardScaler:
    def __init__(self):
        self.mean = None
        self.std = None
        
    def _check_is_array(self, x: np.ndarray) -> np.ndarray:
        """
        Try to convert x to a np.ndarray if it's not a np.ndarray and return. If it can't be cast, raise an error.
        """
        if not isinstance(x, np.ndarray):
            x = np.array(x)
        assert isinstance(x, np.ndarray), "Expected the input to be a numpy array"
        return x
    
    def fit(self, x: np.ndarray) -> None:   
        x = self._check_is_array(x)
        self.mean = np.mean(x, axis=0)
        self.std = np.std(x, axis=0)
        
    def transform(self, x: np.ndarray) -> np.ndarray:
        """
        Standardize the given vector
        """
        x = self._check_is_array(x)
        
        # Handle division by zero
        if np.any(self.std == 0):
            return np.zeros_like(x)
        
        return (x - self.mean) / self.std
    
    def fit_transform(self, x: np.ndarray) -> np.ndarray:
        x = self._check_is_array(x)
        self.fit(x)
        return self.transform(x)
