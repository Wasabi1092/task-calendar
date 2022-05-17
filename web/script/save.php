<?php
              
if(isset($_POST['name']) && isset($_POST['date']) && isset($_POST['subject']))
{
    $name=$_POST['name'];
    $date=$_POST['date'];
    $subject = $_POST['subject'];
    $fp = fopen('/data/data.txt', 'a');
    fwrite($fp, $name);
    fwrite($fp, $date);
    fwrite($fp, $subject);
    fclose($fp);
}
?>