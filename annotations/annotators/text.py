from annotations import stims
from annotations.annotators import Annotator
import numpy as np
from annotations.core import Note
import pandas as pd


class TextAnnotator(Annotator):

    target = stims.TextStim


class TextDictionaryAnnotator(TextAnnotator):

    def __init__(self, dictionary, variables=None, missing='nan'):
        self.data = pd.read_csv(dictionary, sep='\t', index_col=0)
        self.variables = variables
        if variables is not None:
            self.data = self.data[variables]
        # Set up response when key is missing
        self.missing = np.nan
        super(self.__class__, self).__init__()

    def apply(self, stim):
        if stim.text not in self.data.index:
            vals = pd.Series(self.missing, self.variables)
        else:
            vals = self.data.loc[stim.text]
        return Note(stim, self, vals.to_dict())
