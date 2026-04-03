# Generated from kitchen-docker-3.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name kitchen-docker

Name: rubygem-%{gem_name}
Version: 3.0.0
Release: 1%{?dist}
Summary: A Docker Driver for Test Kitchen
License: Apache 2.0
URL: https://github.com/test-kitchen/kitchen-docker
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(cane)
# BuildRequires: rubygem(tailor)
# BuildRequires: rubygem(countloc)
# BuildRequires: rubygem(rspec) >= 3.2
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(rspec-its) >= 1.2
# BuildRequires: rubygem(rspec-its) < 2
# BuildRequires: rubygem(fuubar) >= 2.0
# BuildRequires: rubygem(fuubar) < 3
# BuildRequires: rubygem(simplecov) >= 0.9
# BuildRequires: rubygem(simplecov) < 1
# BuildRequires: rubygem(codecov)
# BuildRequires: rubygem(codecov) < 1
# BuildRequires: rubygem(codecov) >= 0.0.2
# BuildRequires: rubygem(chefstyle)
# BuildRequires: rubygem(kitchen-inspec) >= 2.0
# BuildRequires: rubygem(kitchen-inspec) < 3
# BuildRequires: rubygem(train) >= 2.1
# BuildRequires: rubygem(train) < 4.0
BuildArch: noarch

%description
A Docker Driver for Test Kitchen.


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
# rspec spec
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/.cane
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%{gem_instdir}/.tailor
%{gem_instdir}/.yamllint
%license %{gem_instdir}/LICENSE
%{gem_instdir}/kitchen.windows.yml
%{gem_instdir}/kitchen.yml
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docker.ps1
%doc %{gem_instdir}/kitchen-docker.gemspec
%{gem_instdir}/test

%changelog
* Thu Apr 02 2026 Robby Callicotte <rcallicotte@fedoraproject.org> - 3.0.0-1
- Initial package
