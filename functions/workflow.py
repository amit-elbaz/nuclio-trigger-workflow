from kfp import dsl
from mlrun.platforms import auto_mount
import os
import sys
import mlrun

@dsl.pipeline(name="Decision pipeline", description="Pipeline that runs a function based on ")
def kfpipeline(input_val):

    
    step_1 = mlrun.run_function('func_A')    

    step_2 = mlrun.run_function('func_A').after(step_1)
    
