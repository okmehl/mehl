Thank you for opening an issue with Mehl. Please understand that issues are meant for bugs and enhancement-requests.


To be able to help you best, we need some more information.

## Before you open your issue
- [ ] Check if no issue or pull-request for this already exists.
- [ ] Check documentation and FAQ
- [ ] You understand `Mehl` is made by volunteers in their **free time** — be conscise, civil and accept that delays can occur.
- [ ] The title of the issue should be short and simple. It should contain specific terms related to the actual issue. Be specific while writing the title.

## Environment & Versions
### Environment
 - [ ] kubernetes
 - [ ] docker swarm

### Versions
To find your version, get the image name of a mehl container and read the version from the tag (example for version master).
```
$> docker ps -a | grep mehl
140b09d4b09c    mehl/roundcube:master    "docker-php-entrypoi…"    2 weeks ago    Up 2 days (healthy)    80/tcp
$> grep MEHL_VERSION docker-compose.yml mehl.env
```

## Description
Further explain the bug in a few words. It should be clear what the unexpected behaviour is. Share it in an easy-to-understand language.

## Replication Steps
Steps for replicating your issue

## Expected behaviour
Explain what results you expected - be as specific as possible. Just saying "it doesn’t work as expected" is not useful. It's also helpful to describe what you actually experienced.

## Logs
Often it is very useful to include log fragments of the involved component. You can get the logs via `docker logs <container name> --tail 1000`. For example for the admin container:
`docker logs mehl_admin_1 --tail 1000`

If you can find the relevant section, please share only the parts that seem relevant. If you have any logs, please enclose them in code tags, like so:
````markdown
```
Your logs here!
```
````
