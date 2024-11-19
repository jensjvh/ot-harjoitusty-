from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest -v src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)


@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)