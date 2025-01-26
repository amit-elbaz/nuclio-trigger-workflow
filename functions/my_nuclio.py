import mlrun


def handler(context, event):
    project = mlrun.get_or_create_project("nuclio-trigger-workflow-amite", "../")
    workflow_instance = project.run(
                            name="my-workflow",
                            watch=False,
                            # local=False,
                            engine="kfp",
                    )
    