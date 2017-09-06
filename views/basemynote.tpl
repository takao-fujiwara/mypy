% include('headermynote.tpl')

<body>
 <div class="col-sm-3 col-md-2 sidebar">
		<ul class="nav nav-slider">
			%if request.path == "/mynotes":
				<li class="active"><a href="/mynotes">一覧</a></li>
				<li><a href="/mynotes/add">登録</a></li>
			%elif request.path == "/mynotes/add":
				<li><a href="/mynotes">一覧</a></li>

			%else:
			<li class="active"><a href="/mynotes">一覧</a></li>

			%end
		</ul>
	</div>
{{!basemynote}}




% include("footermynote.tpl")
