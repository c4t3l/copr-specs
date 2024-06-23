# Generated from tty-screen-0.8.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tty-screen

Name: rubygem-%{gem_name}
Version: 0.8.1
Release: 1%{?dist}
Summary: Terminal screen size detection which works on Linux, OS X and Windows/Cygwin platforms and supports MRI, JRuby, TruffleRuby and Rubinius interpreters
License: MIT
URL: https://ttytoolkit.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0.0
# BuildRequires: rubygem(rspec) >= 3.0
BuildArch: noarch

%description
Terminal screen size detection which works on Linux, OS X and Windows/Cygwin
platforms and supports MRI, JRuby, TruffleRuby and Rubinius interpreters.


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
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Sat Sep 17 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 0.8.1-1
- Initial package
