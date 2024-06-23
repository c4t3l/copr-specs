# Generated from winrm-elevated-1.2.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name winrm-elevated

Name: rubygem-%{gem_name}
Version: 1.2.3
Release: 1%{?dist}
Summary: Ruby library for running commands as elevated
License: Apache-2.0
URL: https://github.com/WinRb/winrm-elevated
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3.0
# BuildRequires: rubygem(rspec) >= 3.2
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(rubocop) >= 0.51.0
# BuildRequires: rubygem(rubocop) < 0.52
BuildArch: noarch

%description
Ruby library for running commands via WinRM as elevated through a scheduled
task.


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
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Sat Sep 10 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 1.2.3-1
- Initial package
