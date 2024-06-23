# Generated from tomlrb-2.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tomlrb

Name: rubygem-%{gem_name}
Version: 2.0.3
Release: 1%{?dist}
Summary: A racc based toml parser
License: MIT
URL: https://github.com/fbernier/tomlrb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0
# BuildRequires: rubygem(psych) >= 4
# BuildRequires: rubygem(psych) < 5
BuildArch: noarch

%description
A racc based toml parser.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# Run the test suite.
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Mon Apr 03 2023 Robby Callicotte <rcallicotte@fedoraproject.org> - 2.0.3-1
- Initial package
