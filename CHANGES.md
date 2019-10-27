# Change Log

## v0.1.0

- removed `()` in returns for py3
- added py3 to pack.yaml
- added append_to_address group (requires py3)
- added action to find single ip address object
- updated requirements file to pull update v0.1.0 of PyFortiAPI which supports filters
- added `find_single_address_object` action to avoid searching in jinja

## v0.0.4

- add some read me content for create_address_group action
- remove `repr` from the create_address_group python action to mitigate http 424 errors, included
 working example in README file. Tested on v6.2.2 (contribued by JP Bourget <jp@syncurity.net)

## v0.0.3

- Update "action name" in update_address_group.yaml

## v0.0.2

- Minor linting fix

## v0.0.1

Initial Revision
