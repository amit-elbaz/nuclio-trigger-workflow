# import mlrun
# # import sys
# # sys.path.append("/opt/nuclio")
# # from util.utility import utility_func

# # def init_context(context):
# #     context.logger.info("start init context")
# #     # project = mlrun.load_project(url="git://github.com/amit-elbaz/nuclio-trigger-workflow.git#master", context="./my-loaded-project")
# #     project = mlrun.get_or_create_project("nuclio-trigger-workflow-amite", "./")

# #     setattr(context,"project",project)
    
def test(event):
    # context.logger.info("start handler")
    
    # project = mlrun.get_or_create_project("nuclio-trigger-workflow-amite", "./")
    # workflow_instance = context.project.run(name="my-workflow", engine="remote")
    # workflow_instance = context.project.run(name="my-workflow", watch=False, engine="kfp", dirty=True)
    # job = context.project.run_function("func-a")
    return 1
    # return utility_func()
    # workflow_instance = project.run(workflow_path="/opt/nuclio/workflows/workflow.py")
    



from mlrun.runtimes import nuclio_init_hook


def init_context(context):
    nuclio_init_hook(context, globals(), "serving_v2")


def handler(context, event):
    return context.mlrun_handler(context, event)
