% include('header.tpl')

<body>
 <div class="col-sm-3 col-md-2 sidebar">
		<ul class="nav nav-slider">
			%if request.path == "/books":
				<li class="active"><a href="/books"></a>一覧</li>
				<li><a href="/books/add">登録</a></li>
			%elif request.path == "/books/add":
				<li><a href="/books"></a>一覧</li>

			%else:
			<li class="active"><a href="/books"></a>一覧</li>

			%end
		</ul>
	</div>
{{!base}}




% include("footer.tpl")
