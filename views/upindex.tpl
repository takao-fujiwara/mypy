<!DOCTYPE html>
<html>
<head>
<meta content="text/html; charset=UTF-8" http-equiv="content-type">

    <title>upindex</title>

<style type="text/css">
    ul {
						list-style:none;
			  }
</style>

<script type="text/javascript" language="javascript">
<!--
function OnFileSelect( inputElement )
{
	// ファイルリストを取得
	var fileList = inputElement.files;

	// ファイルの数を取得
	var fileCount = fileList.length;

	var loadCompleteCount = 0;
	var imageList = "";

	// 選択されたファイルの数だけ処理する
	for ( var i = 0; i < fileCount; i++ ) {

		// FileReaderを生成
		var fileReader = new FileReader();

		// ファイルを取得
		var file = fileList[ i ];

		// 読み込み完了時の処理を追加
		fileReader.onload = function() {

			// <li>,<img>タグの生成
			imageList += "<li><img src=\"" + this.result + "\" /></li>\r\n";

			// 選択されたファイルすべの処理が完了したら、<ul>タグに流し込む
			if ( ++loadCompleteCount == fileCount ) {

				// <ul>タグに<li>,<img>を流し込む
				document.getElementById( "ID001" ).innerHTML = imageList;
			}
		};

		// ファイルの読み込み(Data URI Schemeの取得)
		fileReader.readAsDataURL( file );
	}
}
// -->
</script>

</head>

<body>
<form method="POST" action="/upload" enctype="multipart/form-data">
        <fieldset>
        <p><label>title</label><input name="title" type="text"></p>
				<p><labe2>memo</labe2><input name="memo" type="text"></p>

        <input type="file" name="upload" onchange="OnFileSelect( this );" multiple />
        <br><br>
        <input value="Post" type="submit">
        <div><ul id="ID001"></ul><div>

        </div>
        <br><br>

				</fieldset>
    </form>
</body></html>
