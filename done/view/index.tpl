% rebase('base.tpl')
	<div class="container-fluid">
    <div class="main">

	<h6 class="page-header"></h6>

	<div class="table-responsive">
		<table class="table table-striped">
			<thead>
				<tr>
					<th>id</th>
					<th>タイトル</th>
					<th>価格</th>
					<th>メモ</th>
					<th></th>
				</tr>
			</thead>
			<tbody>

				% for book in books:
				<tr>
					<td>{{book.id}}</td>
					<td><a href="/books/{{book.id}}/edit">{{book.title}}</a></td>
					<td>{{book.price}}円</td>
					<td>{{book.memo}}</td>
					<td>
						<form action="/books/{{book.id}}/delete" method="post">
							<p><input value="削除" type="submit"/></p>
						</form>
					</td>
				</tr>
				%end

			</tbody>
		</table>
		</div>
	</div>
