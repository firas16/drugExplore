## Describe your changes



## Checklist before requesting a review

## Documentation

- [ ] The README file is updated  : (Jira ticket, developper name, description and date of the release + documentation link).  
:warning: And old links are updated with new url (jira.devnet.klm.com => afklm.atlassian.net)
- [ ] Files header are updated (do not forget the matricule in the profile file).  => Pas utilisé d’après le support
- [ ] Confluence documentation has been created/updated to reflect the changes

## Readability

- [ ] The code is clear and easy to understand
- [ ] Variable and function names are meaningful
- [ ] Comments are provided where necessary
- [ ] Javadoc documentation is provided for every class, method, and constructor

## Good practices

- [ ] The code does not contain hard-coded values

## Functionnal 

- [ ] The development meets the functional requirements described in the ticket

## Performances
- [ ] The code is optimized for performance.

## Tests

- [ ] Each new function is tested with a unit test
- [ ] Unit tests follow the Given-When-Then format.
- [ ] All use cases are covered
- [ ] The tests pass without errors.
- [ ] The full process has been run in UAT without errors.
- [ ] Check that there is no impact on other jobs/projects

## Teradata 
- [ ] The work scripts are correct (collect stats in resume script etc)

## Ctrl-M 
- [ ] No new error in metrosas : https://metrosasdev.airfrance.fr/metrosas/rapports/batch/ctm/Namingconventionscyc_TLS_LE_BIDCL.html
- [ ] The teradata ressource is added in all Ctrl-m teradata jobs
- [ ] Check the scheduling (it is recommended to avoid 3am-5am / 6pm-8pm time slots)
- [ ] The XXX_BIDCL_ALLDAYS exception calendar is used only if the process can run in UAT.
