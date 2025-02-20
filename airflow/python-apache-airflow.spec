Name:           python-apache-airflow
Version:        2.10.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Programmatically author, schedule and monitor data pipelines

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://airflow.apache.org/
Source:         %{pypi_source apache_airflow}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'apache-airflow' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-apache-airflow
Summary:        %{summary}

%description -n python3-apache-airflow %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-apache-airflow aiobotocore,airbyte,alibaba,all,all-core,all-dbs,amazon,apache-atlas,apache-beam,apache-cassandra,apache-drill,apache-druid,apache-flink,apache-hdfs,apache-hive,apache-iceberg,apache-impala,apache-kafka,apache-kylin,apache-livy,apache-pig,apache-pinot,apache-spark,apache-webhdfs,apprise,arangodb,asana,async,atlas,atlassian-jira,aws,azure,cassandra,celery,cgroups,cloudant,cloudpickle,cncf-kubernetes,cohere,common-compat,common-io,common-sql,databricks,datadog,dbt-cloud,deprecated-api,devel-ci,dingding,discord,docker,druid,elasticsearch,exasol,fab,facebook,ftp,gcp,gcp-api,github,github-enterprise,google,google-auth,graphviz,grpc,hashicorp,hdfs,hive,http,imap,influxdb,jdbc,jenkins,kerberos,kubernetes,ldap,leveldb,microsoft-azure,microsoft-mssql,microsoft-psrp,microsoft-winrm,mongo,mssql,mysql,neo4j,odbc,openai,openfaas,openlineage,opensearch,opsgenie,oracle,otel,pagerduty,pandas,papermill,password,pgvector,pinecone,pinot,postgres,presto,pydantic,qdrant,rabbitmq,redis,s3,s3fs,salesforce,samba,saml,segment,sendgrid,sentry,sftp,singularity,slack,smtp,snowflake,spark,sqlite,ssh,statsd,tableau,tabular,telegram,teradata,trino,uv,vertica,virtualenv,weaviate,webhdfs,winrm,yandex,ydb,zendesk


%prep
%autosetup -p1 -n apache_airflow-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x aiobotocore,airbyte,alibaba,all,all-core,all-dbs,amazon,apache-atlas,apache-beam,apache-cassandra,apache-drill,apache-druid,apache-flink,apache-hdfs,apache-hive,apache-iceberg,apache-impala,apache-kafka,apache-kylin,apache-livy,apache-pig,apache-pinot,apache-spark,apache-webhdfs,apprise,arangodb,asana,async,atlas,atlassian-jira,aws,azure,cassandra,celery,cgroups,cloudant,cloudpickle,cncf-kubernetes,cohere,common-compat,common-io,common-sql,databricks,datadog,dbt-cloud,deprecated-api,devel-ci,dingding,discord,docker,druid,elasticsearch,exasol,fab,facebook,ftp,gcp,gcp-api,github,github-enterprise,google,google-auth,graphviz,grpc,hashicorp,hdfs,hive,http,imap,influxdb,jdbc,jenkins,kerberos,kubernetes,ldap,leveldb,microsoft-azure,microsoft-mssql,microsoft-psrp,microsoft-winrm,mongo,mssql,mysql,neo4j,odbc,openai,openfaas,openlineage,opensearch,opsgenie,oracle,otel,pagerduty,pandas,papermill,password,pgvector,pinecone,pinot,postgres,presto,pydantic,qdrant,rabbitmq,redis,s3,s3fs,salesforce,samba,saml,segment,sendgrid,sentry,sftp,singularity,slack,smtp,snowflake,spark,sqlite,ssh,statsd,tableau,tabular,telegram,teradata,trino,uv,vertica,virtualenv,weaviate,webhdfs,winrm,yandex,ydb,zendesk


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l ...


%check
%pyproject_check_import


%files -n python3-apache-airflow -f %{pyproject_files}


%changelog
%autochangelog