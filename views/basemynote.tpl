% include('headermynote.tpl')

<body>
 <div class="col-sm-3 col-md-2 sidebar">
		<ul class="nav nav-slider">
			%if request.path == "/mynotes":
				<li class="active"><a href="/mynotes">一覧</a></li>
				<li><a href="/upload">登録</a></li>
			%elif request.path == "/mynotes/":
				<li><a href="/mynotes">一覧</a></li>

			%else:
			<li class="active"><a href="/mynotes">一覧</a></li>

			%end
		</ul>
	</div>
{{!base}}




% include("footermynote.tpl")
