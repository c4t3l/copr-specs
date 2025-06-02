# Generated from kitchen-ansible-0.56.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name kitchen-ansible

Name: rubygem-%{gem_name}
Version: 0.56.0
Release: 1%{?dist}
Summary: ansible provisioner for test-kitchen
License: Apache-2.0
URL: https://github.com/neillturner/kitchen-ansible
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(rspec)
# BuildRequires: rubygem(pry)
BuildArch: noarch

%description
== DESCRIPTION:
Ansible Provisioner for Test Kitchen
== FEATURES:
Supports running ansible-playbook.
.


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
%{gem_libdir}
%{gem_instdir}/provisioner_options.md
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/kitchen-ansible.gemspec

%changelog
* Mon Jun 02 2025 Robby Callicotte <rcallicotte@fedoraproject.org> - 0.56.0-1
- Initial package
