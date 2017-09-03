% include('header.tpl')

<body>
 <div class="col-sm-3 col-md-2 sidebar">
		<ul class="nav nav-slider">
			%if request.path == "/books":
				<li class="active"><a href="/books">一覧</a></li>
				<li><a href="/books/add">登録</a></li>
			%elif request.path == "/books/add":
				<li><a href="/books">一覧</a></li>

			%else:
			<li class="active"><a href="/books">一覧</a></li>
			
			%end
		</ul>
	</div>
{{!base}}




% include("footer.tpl")
