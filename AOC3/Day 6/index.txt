<?php session_start();
$flag = "THM{791d43d46018a0d89361dbf60d5d9eb8}";
include("./includes/creds.php");
if($_SESSION['username'] === $USER){                        
	header( 'Location: manage.php' );
	die();
} else {
	$labNum = "";
  require "./includes/header.php";
?>
<div class="row">
  <div class="col-lg-12">
  </div>
  <div class="col-lg-8 col-offset-1">
      <?php if (isset($error)) { ?>
          <span class="text text-danger"><b><?php echo $error; ?></b></span>
      <?php }

?>
 <p>Welcome <?php echo getUserName(); ?></p>
	<div class="alert alert-danger" role="alert">This server has sensitive information. Note All actions to this server are logged in!</div> 
	</div>
<?php if($errInclude){ include($_GET['err']);} ?>
</div>

<?php
}
?>