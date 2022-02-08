@Library('lib@2.0') import com.*
def startHour = Integer.parseInt(getBuildTime("HH"));
def buildParams = getBuildParams(params);
print buildParams;

stage ('PClint'){
    node {
        ck1 = build job: 'pclint_test', parameters: buildParams, propagate: false
        setStageBuild('PClint', ck1, '');
    }
}

stage ('compile'){
    parallel 'compile1':{
        node {
   if (params.Build == 'ALL'||params.Build == 'compile_bcm6755_11ax'){
    cc1 = build job: 'compile_bcm6755_11ax',parameters: buildParams, propagate: false
    setStageBuild('compile', cc1, 'bcm6755_11ax');
    }
   }
    },'compile2':{
        node {
   if (params.Build == 'ALL'||params.Build == 'compile_bcm6755_11ax_mesh'){
    cc1 = build job: 'compile_bcm6755_11ax_mesh',parameters: buildParams, propagate: false
    setStageBuild('compile', cc1, 'bcm6755_11ax_mesh');
    }
        }
    },'compile3':{
        node {
   if (params.Build == 'ALL'||params.Build == 'compile_bcm6756_11ax'){
    cc1 = build job: 'compile_bcm6756_11ax',parameters: buildParams, propagate: false
    setStageBuild('compile', cc1, 'bcm6756_11ax');
    }
        }
    },'compile4':{a
        node {
   if (params.Build == 'ALL'||params.Build == 'compile_qca9563_qca8334_mesh'){
    cc1 = build job: 'compile_qca9563_qca8334_mesh',parameters: buildParams,propagate: false
    setStageBuild('compile', cc1, 'qca9563_qca8334_mesh');
    }
        }
    },'compile5':{
        node {
   if (params.Build == 'ALL'||params.Build == 'compile_rtl8197gh'){
    cc1 = build job: 'compile_rtl8197gh',parameters: buildParams,propagate: false
    setStageBuild('compile', cc1, 'rtl8197gh');
    }
        }
    },'compile6':{
        node {
   if (params.Build == 'ALL'||params.Build == 'compile_rtl8198d_mesh'){
    cc1 = build job: 'compile_rtl8198d_mesh',parameters: buildParams,propagate: false
    setStageBuild('compile', cc1, 'rtl8198d_mesh');
    }
        }
    },'compile7':{
        node {
   if (params.Build == 'ALL'||params.Build == 'qca4019_qca9988_mesh'){
    cc1 = build job: 'qca4019_
   }
        }
    }
}