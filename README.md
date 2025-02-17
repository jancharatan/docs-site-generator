# docs-site-generator

A GitHub action that takes stuff from markdown files in my Google Drive and builds my personal site from that.

### How to use

1. Create the folder that you want to use to populate your site. In my case, I just created a folder called `docs-site-generator` in my person drive account.

2. Create a Google cloud service account. Copy the `service_account.json` file and also take note of the email associated with the service account.

3. Share the folder created in step #1 with the service account so that the service account can read the files when the action runs.

4. Add `SERVICE_ACCOUNT_JSON` as an action secret. It's just the contents of the json file you received when you created the service account.

5. Add `ACCESS_TOKEN` as an action secret. This should be an access token with write access to the repo where the output is going to live. In my case, that's just `jancharatan/jancharatan.github.io`. If you fork the repo, you'd have to obviously change that in the `generate-site.yml` file.

6. Run the action. Within the repo that has the actual output, make sure to set up github sites. The page should update automatically every time the action runs.

### My site

[jancharatan.github.io](https://jancharatan.github.io/)
