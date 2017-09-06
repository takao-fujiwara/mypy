% rebase('basemynote.tpl')
	<div class="container-fluid">
    <div class="main">

	<h6 class="page-header"></h6>

	<div class="table-responsive">
		<table class="table table-striped">
			<thead>
				<tr>
					<th>id</th>
					<th>タイトル</th>
					<th>メモ</th>
					<th>ファイル名</th>
					<th></th>
				</tr>
			</thead>
			<tbody>

				% for mynote in mynotes:
				<tr>
					<td>{{mynote.id}}</td>
					<td><a href="/mynotes/{{mynote.id}}/edit">{{mynote.title}}</a></td>
					<td>{{mynote.memo}}</td>
					<td>{{mynote.fname}}</td>
					<td>
						<form action="/mynotes/{{mynote.id}}/delete" method="post">
							<p><input value="削除" type="submit"/></p>
						</form>
					</td>
				</tr>
				%end

			</tbody>
		</table>
		</div>
	</div>
