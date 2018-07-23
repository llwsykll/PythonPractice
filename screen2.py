function getArticleTypeByDept(staffId,departmentId,articleType,oaBaseUrl,article) {
	console.log(article);
	var _optDeptRole = 0;
  $(departmentId).on('change', function () {
    var path = $(oaBaseUrl).val();
    var deptId = $(departmentId).find('option:selected').val();
    if (deptId != 5) {
                if (staffId) {
                $.ajax({
                  url:path+'/department/role',
                  type:'POST',
                  dataType: 'json',
                  contentType: 'application/json;charset=UTF-8',
                  data:JSON.stringify({
                       "departmentId": deptId,
                        "staffId": $(staffId).val()	
                  }),
                  success: function (resDeptRole) {
                      if(resDeptRole.data != "部门分管领导"){
                        _optDeptRole = 1;
						$(articleType).find('option[value="1140"]').remove();
					}
                    if ($(articleType).val()) {
                      $(articleType).val('').trigger('change');
                    }
                  }
                })
              }
    }
	else{
		var flag = false;
		console.log($(articleType).find('option[value="1140"]'));
		var options = $(articleType).find('option');
		console.log(options.length);
		console.log(options);
		for(var i=0;i<options.length;i++){
			console.log('option',options[i]);
			if(options[i].value==1140){
			flag=true;}
		}
		if(options.length == 3){
			var html='<option value="1140">监管部门文件1</option>';
			$(articleType).append(html);
		}
	}
  });
}