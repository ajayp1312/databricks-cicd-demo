# Databricks Sales CI/CD Demo

A beginner project for deploying a notebook and job to Azure Databricks using GitHub Actions.

## Project Structure

```
databricks-cicd-demo/
├── README.md
├── .gitignore
├── databricks.yml              # Bundle configuration
├── src/
│   └── sales_summary.py        # Sample notebook
└── .github/
    └── workflows/
        └── databricks-cicd.yml # CI/CD workflow
```

## What this project does

1. Creates a sales summary notebook with sample data.
2. Defines a single-node job cluster.
3. Deploys via GitHub Actions.
4. Optionally executes the notebook.

## Workflow events

| Event | Action |
|-------|--------|
| Pull request into `main` | Check Python syntax |
| Merge to `main` | Validate and deploy bundle |
| Manual workflow run | Deploy and optionally execute notebook |

## Setup

### 1. Add Databricks credentials to GitHub

**Settings → Secrets and variables → Actions → New repository secret**

| Secret name | Value |
|---|---|
| `DATABRICKS_HOST` | Your workspace base URL |
| `DATABRICKS_TOKEN` | Your Databricks personal access token |

### 2. Check supported compute

Verify your workspace allows:
- Runtime: `15.4.x-scala2.12`
- Node type: `Standard_Ds3_v2`

If not available, edit `databricks.yml` with your workspace's allowed compute.

## Expected notebook output

| Region | Total sales |
|--------|-------------|
| North  | 150         |
| South  | 80          |

Then: `SUCCESS: sales totals are correct.`

## Important

- **Executing the notebook uses Databricks compute and may incur charges.**
- Check your Azure subscription and quota before running.
- For production, use service principals or OAuth instead of personal access tokens.

## References

- [Databricks Bundles](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/bundles)
- [Databricks with GitHub Actions](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/ci-cd/github)