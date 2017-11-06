% rebase('basemynote.tpl')

  <div class="col-md-5">

	%if request.path == "/mynotes/upload/":
	  <form action="/mynotes/upload" method="post">
	  <h3 class="page-header">登録</h3>

	%else:
	  <form action="/mynotes/{{mynote.id}}/edit" method="post">
		<h4 class="page-header">編集<input type="submit" class="btn btn-default" value="（更新する）"/></h4>
	%end


	  <div class="form-group">
				{{!form.title.label}}
				{{!form.title(class_="form-control", placeholder=u"タイトルを入力", maxlength="100")}}

				%if form.title.errors:
					<div class="errors">
						% for error in form.title.errors:
							<p class="text-danger">{{error}}</p>
						% end
					</div>
				%end

				</div>

				<div class="form-group">

 				{{!form.memo.label}}
 				{{!form.memo(class_="form-control",	placeholder=u"メモを入力", maxlength="100")}}

 				% if form.memo.errors:
 					<div class="errors">
 						% for error in form.memo.errors:
 							<p class="text-danger">{{error}}</p>
 						% end
 					</div>
 				% end

 				</div>

				<div class="form-group">
						{{!form.fname.label}}
						{{!form.fname(class_="form-control", placeholder=u"ファイル名を入力", maxlength="100")}}

						%if form.fname.errors:
							<div class="errors">
								% for error in form.fname.errors:
									<p class="text-danger">{{error}}</p>
								% end
							</div>
						%end

				</div>

<div class="static-image">
	<img src="/static/img/{{mynote.fname}}" alt="画像なし" width="250" height="150">
</div>





				</form>
	</div>
