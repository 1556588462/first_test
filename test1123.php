    <?php
    class Person
    {
        var $name;
        var $height;
        function __construct()
        {
            echo 'Person类的构造函数被调用了';
        }
    }
    $zhangsan = new Person();
    $zhangsan->name = "张三";
    $zhangsan->height = 180;
    $zhangsan->weight = 75;



    $s = 'O:6:"Person":3:{s:4:"name";s:6:"张三";s:6:"height";i:180;s:6:"weight";i:75;}';
    $lisi = unserialize($s);
    var_dump($lisi);
    ?>