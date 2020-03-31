# CITerm
CITerm is a Terminal for **[CodeIgniter](https://github.com/bcit-ci/CodeIgniter)**, used  to generate customized models, views and controllers. Easy to use, just **place CITerm script and Templates folder into the project's main directory**.

## How to use
- Run & Generate the file. `php CITerm.php <type> <value>`
> `php CITerm.php controller Mycontroller1`
- or Run it.
> `php CITerm.php`
- then Generate  the file `<type> <name>`
> `model Mymodel2`
- or type `help`

```
php CITerm.php [type] [value]
[type]:
    controller            Create a new controller.
    model                 Create a new model.
    view                  Create a new view.

[value]:
    filename              Any valid filename.

```

## Template Customization
```
<?php
class {NAME} extends CI_Model{

  function __construct()
  {
    parent::__construct();
  }

}
```
- '`{NAME}`' is a placeholder for the classname.

## Note
- Make sure to place CITerm script and Templates folder into the **project's main directory**.

## Tested on
- Windows 10

<br>For any suggestion email me on [mohab.elsheikh@gmail.com](mailto:mohab.elsheikh@gmail.com).
<br>Feel free to use it.
