# import mlrun
from util import utility_func
# def init_context(context):
#     context.logger.info("start init context")
#     project = mlrun.load_project(url="git://github.com/amit-elbaz/nuclio-trigger-workflow.git#master", context="./my-loaded-project")
#     setattr(context,"project",project)
    
def handler(context, event):
    context.logger.info("start handler")
    return utility_func
    # project = mlrun.get_or_create_project("nuclio-trigger-workflow-amite", "/opt/nuclio")
    # project = mlrun.get_current_project()
    # workflow_instance = context.project.run(name="my-workflow", watch=False, engine="kfp")
    # workflow_instance = project.run(workflow_path="/opt/nuclio/workflows/workflow.py")
    
