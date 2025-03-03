import mlrun
# import sys
# sys.path.append("/opt/nuclio")
from util.utility import utility_func
# def init_context(context):
#     context.logger.info("start init context")
#     project = mlrun.load_project(url="git://github.com/amit-elbaz/nuclio-trigger-workflow.git#master", context="./my-loaded-project")
#     setattr(context,"project",project)
    
def handler(context, event):
    context.logger.info("start handler")
    
    project = mlrun.get_or_create_project("nuclio-trigger-workflow-amite", "./")
    workflow_instance = project.run(name="my-workflow", watch=False, engine="kfp", dirty=True)
    return utility_func()
    # workflow_instance = project.run(workflow_path="/opt/nuclio/workflows/workflow.py")
    
