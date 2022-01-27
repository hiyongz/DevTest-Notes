//function: 自动将传入到pipeline参数数组转换为map结构数组，供给调用的job使用
//@Library('lib@2.0') import com.*
//def buildParams = getBuildParams(params);
//build job: 'xxx', parameters: buildParams

//enter:
//不用传参也可以直接访问:params
def call(params) {    
	    
    def buildParams = [];
    def curParam = null;
	//println "++++++++++";
    //println params.size();
    //params.each{    
    for(it in params){
        //println it;
        //println it.getKey() + ":" + it.getValue().toString();        
        if(it.getValue().toString().equals("true") || it.getValue().toString().equals("false")){
            //println "is boolean";
            //类型不对： java.lang.ClassCastException: hudson.model.BooleanParameterValue.value expects boolean but received class java.lang.String
            //curParam = [$class: 'BooleanParameterValue', name: it.getKey(), value: it.getValue()]; 
            if(it.getValue().toString().equals("true"))
                curParam = [$class: 'BooleanParameterValue', name: it.getKey(), value: true]; 
            else     
                curParam = [$class: 'BooleanParameterValue', name: it.getKey(), value: false]; 
        } else {
            //println "is string";
            curParam = [$class: 'StringParameterValue', name: it.getKey(), value: it.getValue()];
        }
        buildParams << curParam;
    }
    //println "++++++++++";
    
    //def buildParams = [[$class: 'StringParameterValue', name: 'main_version', value: params.main_version], []];
    return buildParams;
}

