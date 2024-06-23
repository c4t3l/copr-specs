# Generated from rexml-3.2.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rexml

Name: rubygem-%{gem_name}
Version: 3.2.5
Release: 1%{?dist}
Summary: An XML toolkit for Ruby
License: BSD-2-Clause
URL: https://github.com/ruby/rexml
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%description
An XML toolkit for Ruby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{gem_name}-%{version}

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
ruby -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd


%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/NEWS.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/doc


%changelog
* Sat Sep 24 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 3.2.5-1
- Initial package
