# Generated from test-kitchen-3.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name test-kitchen

Name: rubygem-%{gem_name}
Version: 3.6.0
Release: 1%{?dist}
Summary: An integration tool for testing infrastructure code
License: Apache-2.0
URL: https://kitchen.ci/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 3.3
# BuildRequires: rubygem(rb-readline)
# BuildRequires: rubygem(aruba) >= 0.11
# BuildRequires: rubygem(aruba) < 3.0
# BuildRequires: rubygem(fakefs) >= 1.0
# BuildRequires: rubygem(fakefs) < 2
# BuildRequires: rubygem(minitest) >= 5.3
# BuildRequires: rubygem(minitest) < 6
# BuildRequires: rubygem(minitest) < 5.16
# BuildRequires: rubygem(mocha) >= 1.1
# BuildRequires: rubygem(mocha) < 2
# BuildRequires: rubygem(cucumber) >= 2.1
# BuildRequires: rubygem(cucumber) < 8.0
# BuildRequires: rubygem(countloc) >= 0.4
# BuildRequires: rubygem(countloc) < 1
# BuildRequires: rubygem(maruku) >= 0.6
# BuildRequires: rubygem(maruku) < 1
BuildArch: noarch

%description
Test Kitchen is an integration tool for developing and testing infrastructure
code and software on isolated target platforms.


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


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# cucumber
# ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/kitchen
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/support
%{gem_instdir}/templates
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/test-kitchen.gemspec

%changelog
* Sun Jun 23 2024 Robby Callicotte <rcallicotte@fedoraproject.org> - 3.6.0-1
- Rebased to new version

* Sat Sep 10 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 3.3.2-1
- Initial package
