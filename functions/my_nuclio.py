import mlrun


def handler(context, event):
    # project = mlrun.get_or_create_project("nuclio-trigger-workflow-amite", "/opt/nuclio")
    project = mlrun.load_project(url="git://github.com/amit-elbaz/nuclio-trigger-workflow.git#master")
    # project = mlrun.get_current_project()
    workflow_instance = project.run(name="my-workflow", watch=False, engine="kfp")
    # workflow_instance = project.run(workflow_path="/opt/nuclio/workflows/workflow.py")
    
